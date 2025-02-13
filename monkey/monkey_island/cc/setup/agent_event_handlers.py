from common import DIContainer
from common.agent_events import CredentialsStolenEvent
from common.event_queue import IAgentEventQueue
from monkey_island.cc.agent_event_handlers import (
    save_event_to_event_repository,
    save_stolen_credentials_to_repository,
)
from monkey_island.cc.repository import IAgentEventRepository, ICredentialsRepository


def setup_agent_event_handlers(container: DIContainer):
    _subscribe_and_store_to_event_repository(container)


def _subscribe_and_store_to_event_repository(container: DIContainer):
    agent_event_queue = container.resolve(IAgentEventQueue)

    save_event_subscriber = save_event_to_event_repository(container.resolve(IAgentEventRepository))
    agent_event_queue.subscribe_all_events(save_event_subscriber)

    save_stolen_credentials_subscriber = save_stolen_credentials_to_repository(
        container.resolve(ICredentialsRepository)
    )
    agent_event_queue.subscribe_type(CredentialsStolenEvent, save_stolen_credentials_subscriber)
