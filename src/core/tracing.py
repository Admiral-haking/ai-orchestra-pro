from __future__ import annotations

from typing import Any

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def setup_tracing(cfg: dict[str, Any]):
    otel = (cfg.get("observability", {}).get("otel", {}) if cfg else {})
    if not otel or not otel.get("enabled", False):
        return None

    endpoint = otel.get("endpoint")
    resource = Resource.create({"service.name": "ai-orchestra-pro"})
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint))
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer(__name__)

