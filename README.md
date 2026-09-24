# Take-2

Take-2 is a clean-room research operating kernel.

It does not copy the legacy Reaserch repository. Capabilities migrate only after they
demonstrate value under an explicit experiment.

Current phase: bootstrap.

Core design target:

**Observe -> PD -> Diagnose/Understand -> Decide -> Transition -> Verify -> Observe**

PD is not an add-on audit layer. The demonstrated PD operations are intended to be part
of the kernel's reasoning/control loop. Only capabilities with adequate evidence are
promoted into the stable kernel; experimental capabilities remain explicitly typed.

The legacy repository remains authoritative for every capability and project not yet
admitted to Take-2.
