from __future__ import annotations
from pathlib import Path
from typing import Any, Literal
import yaml
from pydantic import BaseModel, Field


class Scene(BaseModel):
    id: str
    kind: str
    narration: str = ""
    shows: str = Field(default="", description="What this visual explains (production gate A3)")
    params: dict[str, Any] = Field(default_factory=dict)
    min_duration: float = 3.0
    pad_after: float = 0.7
    caption: str | None = None
    source: str | None = None


class Source(BaseModel):
    name: str
    url: str = ""
    accessed: str = ""
    license: str = ""
    primary: bool = False
    note: str = ""


class Disclosure(BaseModel):
    altered_or_synthetic: bool = False
    rationale: str = ""


class Gate(BaseModel):
    """Content gate (manual judgement by the Claude session). All must be true for QC_PASS."""
    original_narrative: bool = False
    sources_verified: bool = False
    visuals_explain: bool = False
    distinct_from_previous: bool = False
    title_thumbnail_honest: bool = False
    ad_suitability_noted: bool = False
    licenses_recorded: bool = False
    notes: str = ""

    def all_ok(self) -> bool:
        return all(
            getattr(self, k)
            for k in (
                "original_narrative", "sources_verified", "visuals_explain", "distinct_from_previous",
                "title_thumbnail_honest", "ad_suitability_noted", "licenses_recorded",
            )
        )


class ShortSpec(BaseModel):
    title: str
    scenes: list[Scene]


class Thumbnail(BaseModel):
    variants: list[dict[str, Any]] = Field(default_factory=list)  # {headline, sub, scene, t}
    chosen: int = 0


class Episode(BaseModel):
    id: str
    title: str
    thesis: str = ""
    format: Literal["long", "short"] = "long"
    language: str = "en-us"
    voice: str = "af_heart"
    speed: float = 1.0
    description: str = ""
    tags: list[str] = Field(default_factory=list)
    playlist: str = ""
    ad_suitability_note: str = ""
    audience_made_for_kids: bool = False
    publish_at_utc: str = ""
    disclosure: Disclosure = Field(default_factory=Disclosure)
    sources: list[Source] = Field(default_factory=list)
    data_files: dict[str, str] = Field(default_factory=dict)  # key -> relative csv path
    scenes: list[Scene]
    short: ShortSpec | None = None
    thumbnail: Thumbnail = Field(default_factory=Thumbnail)
    gate: Gate = Field(default_factory=Gate)

    @classmethod
    def load(cls, path: Path) -> "Episode":
        with open(path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        return cls.model_validate(raw)

    def scenes_for(self, fmt: str) -> list[Scene]:
        if fmt == "short":
            if not self.short:
                raise ValueError(f"{self.id}: no `short` section defined")
            return self.short.scenes
        return self.scenes


FORMATS = {"long": (1920, 1080), "short": (1080, 1920)}
FPS = 30
