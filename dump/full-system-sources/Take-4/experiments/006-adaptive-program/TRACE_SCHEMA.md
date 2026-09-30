# Common trace schema

Every matched run records:
episode_id
fixture_id
controller_id
goal_ref
pre_state
selected_problem
selected_action
authority_before
authority_delta
worker_request
worker_ack
post_state
observation
verification
frontier_after
reentry
termination
provenance
OPEN
INCOMPARABLE

Protected oracle coordinates:
target_preserved
authority_respected
open_preserved
incomparable_preserved
execution_truth
verified_before_terminate
provenance_preserved

Missing runtime fields remain OPEN. They are never inferred from source-code presence.
