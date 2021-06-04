```
 SimpleSlotWorker interface:84
   BlockImport typedef:86
   SyncOracle typedef:90
   CreateProposer typedef:93
   Proposer typedef:97
   Claim typedef:100
   EpochData typedef:103
   logging_target(&self) -> &'static str method:106
   block_import(&self) -> Arc<Mutex<Self::BlockImport>> method:109
   epoch_data( &self, header: &B::Header, slot_number: u64, ) -> Result<Self::EpochData, sp_consensus::Error> method:113
   authorities_len(&self, epoch_data: &Self::EpochData) -> Option<usize> method:121
   claim_slot( &self, header: &B::Header, slot_number: u64, epoch_data: &Self::EpochData, ) -> Option<Self::Claim> method:124
   notify_slot( &self, _header: &B::Header, _slot_number: u64, _epoch_data: &Self::EpochData, ) method:133
   pre_digest_data( &self, slot_number: u64, claim: &Self::Claim, ) -> Vec<sp_runtime::DigestItem<B::Hash>> method:141
   block_import_params(&self) -> Box< dyn Fn( B::Header, &B::Hash, Vec<B::Extrinsic>, StorageChanges<<Self::BlockImport as BlockImport<B>>::Transaction, B>, Self::Claim, Self::EpochData, ) -> Result< sp_consensus::BlockImportParams<B, <Self::BlockImport as BlockImport<B>>::Transaction>, sp_consensus::Error > + Send + 'static > method:148
   force_authoring(&self) -> bool method:163
   should_backoff(&self, _slot_number: u64, _chain_head: &B::Header) -> bool method:171
   sync_oracle(&mut self) -> &mut Self::SyncOracle method:176
   proposer(&mut self, block: &B::Header) -> Self::CreateProposer method:179
   slot_remaining_duration(&self, slot_info: &SlotInfo) -> Duration method:182
   proposing_remaining_duration( &self, _head: &B::Header, slot_info: &SlotInfo, ) -> Option<Duration> method:192
   on_slot( &mut self, chain_head: B::Header, slot_info: SlotInfo, ) -> Pin<Box<dyn Future<Output = Option<SlotResult<B>>> + Send>> where <Self::Proposer as Proposer<B>>::Proposal: Unpin + Send + 'static, method:201
```

```
----------|----------|-----------|-----------|--------------------------------------------
        S_i        S_i+1       S_i+2       S_i+3
```

### 出块流程

SimpleSlotWorker 产生一个 Stream 每间隔一个 Slot 开始执行出块逻辑。

client/consensus/babe/src/lib.rs::start_babe()
|
\|/
client/consensus/slots/src/lib.rs::start_slot_worker()

1. 首先对 Slot 时间进行切分:
   - slot_remaining_duration: 这个 slot 还有多长时间，`slot.ends_at - now()`
   - proposing_remaining_duration: 等于 slot_remaining_duration
2. 获取 epoch_data，获取出块必要的一些信息
3. 判断是否/能够出块
   - 如果不是强制出块则继续下面的判断 force_authoring
   - `self.sync_oracle().is_offline()` 是否正在同步
   - 如果验证人大于 1

也就是如果验证人数大于 1,但是正在同步，又不是强制出块，那么此时跳过出块。 4. 拿到 `claim_slot`, 这里面跟 PoW 类似，如果 VRF 产生一个值小于一个阈值，那么就拿到 slot 可以继续出块。
具体实现在 client/consensus/babe/src/authorship.rs::claim_slot()

- 首先尝试拿 primary slot, 如果拿不到尝试 secondary slot.
- parimary slot 是对 VRF 的输出与阈值作比较，小于阈值则拿到。`check_primary_threshold()`
- 如果计算阈值https://github.com/paritytech/substrate/blob/5c70d7bb2b78d4ed5e3aa4fd0449cc6c81d3db98/client/consensus/babe/src/authorship.rs#L26

5. `should_backoff` 判断是否确认高度落后但是又没有落后的太多。如果当前 slot 还在 interval 区间内，backoff.
6. `let logs = self.pre_digest_data(slot_number, &claim);` 提取出块人信息。
7. `proposer.propose()` 然后开始打包区块。
   打包是一个 future, 同时还有一个时间为 slot 时间的延迟 future, 如果 propose 超过了区块时间没有返回，那么就会触发延时的 future, 此时就会报 took too long 的错误，提前返回。
8. 如果区块打包成功, 开始导入区块 `block_import`

### 区块打包

区块打包逻辑在 client/basic-authorship/src/basic_authorship.rs

basic_authorship.rs 里面定义了一个结构体 `Proposer` 实现了 propose

`proposer.propose()` 里面新开了一个 blocking 的线程用户组建区块，最大时长为 2/3 块时间，因为还要留一点时间给验证和确认 1/3.

1. 首先是打包内部交易, 如果内部交易失败直接返回失败。
2. 从交易池 push 交易, `BlockBuilder.push(tx)` 一直到区块满了。
   client/block-builder/src/lib.rs > BlockBuilder.

   在 push 交易的时候，已经执行了一遍交易。

   ```
   /// Push onto the block's list of extrinsics.
   ///
   /// This will ensure the extrinsic can be validly executed (by executing it).
   pub fn push(&mut self, xt: <Block as BlockT>::Extrinsic) -> Result<(), ApiErrorFor<A, Block>> {
   	let block_id = &self.block_id;
   	let extrinsics = &mut self.extrinsics;

   	self.api.execute_in_transaction(|api| {
   		match api.apply_extrinsic_with_context(
   			block_id,
   			ExecutionContext::BlockConstruction,
   			xt.clone(),
   		) {
   			Ok(Ok(_)) => {
   				extrinsics.push(xt);
   				TransactionOutcome::Commit(Ok(()))
   			}
   			Ok(Err(tx_validity)) => {
   				TransactionOutcome::Rollback(
   					Err(ApplyExtrinsicFailed::Validity(tx_validity).into()),
   				)
   			},
   			Err(e) => TransactionOutcome::Rollback(Err(e)),
   		}
   	})
   }
   ```

3. `BlockBuilder.build()` 将 push 的所有交易一起真正打包产生一个区块。

4. 最后做一下块检查，比如 parent_hash, 块大小，块高。

bin/node/cli/src/service.rs

block_import() 初始化 block_import

### Runtime <-> Client call

`primitives/api/src/lib.rs`: 里面定义了 Client 调用 Runtime 内部需要的组件

client.rs 实现了

executor: native executor, wasm executor

可编程的存储网络: https://medium.com/@ppio
