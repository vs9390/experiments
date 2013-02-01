from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig
from orig_config import check_stale_entries

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(cmdline='./pox.py --verbose --no-cli sts.syncproto.pox_syncer openflow.discovery openflow.spanning_tree forwarding.l2_multi sts.util.socket_mux.pox_monkeypatcher openflow.of_01 --address=__address__ --port=__port__', address='127.0.0.1', port=6633, cwd='pox', sync='tcp:localhost:18900')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=4",
                 patch_panel_class=BufferedPatchPanel,
                 dataplane_trace="exp/fuzz_pox_4mesh_blackhole/dataplane.trace",
                 multiplex_sockets=True)

control_flow = EfficientMCSFinder(simulation_config, "exp/fuzz_pox_4mesh_blackhole/events.trace",
                                  invariant_check=check_stale_entries,
                                  wait_on_deterministic_values=False)
