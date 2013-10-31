from config.experiment_config_lib import ControllerConfig
from sts.control_flow import Fuzzer
from sts.input_traces.input_logger import InputLogger
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig
from sts.topology import MeshTopology, FatTree

# Use NOX as our controller
command_line = "./nox_core -v -i ptcp:6635 routing"
controllers = [ControllerConfig(command_line, cwd="nox_classic/build/src", address="127.0.0.1", port=6635)]

# exp_name = "nox_mesh_4_loop"
topology_class = MeshTopology
topology_params = "num_switches=4"
# dataplane_trace = "dataplane_traces/ping_pong_same_subnet_4_switches.trace"
# dataplane_trace = "dataplane_traces/ping_pong_fat_tree.trace"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params)
           #                          dataplane_trace=dataplane_trace)

#simulation_config = SimulationConfig(controller_configs=controllers,
#                                     dataplane_trace=dataplane_trace)

# Use a Fuzzer (already the default)
control_flow =  Fuzzer(
                       simulation_config, input_logger=InputLogger(),
                       fuzzer_params="experiments/nox_mesh_4_loop/fuzzer_params.py",
                       check_interval=20,
                       halt_on_violation=True,
                       steps=300,
                       invariant_check_name="check_for_loops_or_connectivity")