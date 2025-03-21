from collections import OrderedDict
from typing import Final

from localstack.aws.api.stepfunctions import Arn
from localstack.services.stepfunctions.backend.activity import Activity
from localstack.services.stepfunctions.backend.alias import Alias
from localstack.services.stepfunctions.backend.execution import Execution
from localstack.services.stepfunctions.backend.state_machine import StateMachineInstance
from localstack.services.stores import AccountRegionBundle, BaseStore, LocalAttribute


class SFNStore(BaseStore):
    # Maps ARNs to state machines.
    state_machines: Final[dict[Arn, StateMachineInstance]] = LocalAttribute(default=dict)
    # Map Alias ARNs to state machine aliases
    aliases: Final[dict[Arn, Alias]] = LocalAttribute(default=dict)
    # Maps Execution-ARNs to state machines.
    executions: Final[dict[Arn, Execution]] = LocalAttribute(
        default=OrderedDict
    )  # TODO: when snapshot to pods stop execution(?)
    activities: Final[OrderedDict[Arn, Activity]] = LocalAttribute(default=dict)


sfn_stores: Final[AccountRegionBundle] = AccountRegionBundle("stepfunctions", SFNStore)
