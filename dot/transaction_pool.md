core/transaction-pool/graph/src/pool.rs
    - pub struct Pool<B: ChainApi>

        ```
/// Extrinsics pool.
pub struct Pool<B: ChainApi> {
	api: B,
	listener: RwLock<Listener<ExHash<B>, BlockHash<B>>>,
	pool: RwLock<base::BasePool<
		ExHash<B>,
		ExtrinsicFor<B>,
	>>,
	import_notification_sinks: Mutex<Vec<mpsc::UnboundedSender<()>>>,
	rotator: PoolRotator<ExHash<B>>,
}
        ```


```
	/// Get an iterator for ready transactions ordered by priority
	pub fn ready(&self) -> impl Iterator<Item=TransactionFor<B>> {
```

core/service/src/components.rs

base_pool


ServiceTrait

transaction pool

build_network_protocol

import_queue

Components

core/service/src/lib.rs


impl<Components: components::Components> Service<Components> {

	/// Creates a new service.
	pub fn new(
		mut config: FactoryFullConfiguration<Components::Factory>,
		task_executor: TaskExecutor,
	)
	
