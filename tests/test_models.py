from pathlib import Path
from ytf.models import Episode
from ytf import paths


def test_ep001_loads_and_gate_fields():
    ep = Episode.load(paths.CONTENT / "ep-001" / "episode.yaml")
    assert ep.id == "ep-001" and len(ep.scenes) >= 8
    assert all(s.shows for s in ep.scenes), "every scene must say what its visual explains (gate A3)"
    assert ep.short and len(ep.short.scenes) >= 2
    assert (paths.CONTENT / "ep-001" / ep.data_files["nightingale"]).exists()
    assert isinstance(ep.gate.all_ok(), bool)
