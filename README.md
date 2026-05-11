AI-Orchestra Pro
=================

پروژه چندعاملی «Enterprise-grade» با ساختار ماژولار، قابل‌تست، چند‌ارائه‌دهنده (OpenAI/DeepSeek)، قابل مشاهده‌سازی (observability) و ایمن.

راه‌اندازی سریع
----------------
- پیش‌نیاز: Python 3.11+
- تنظیم متغیرها: فایل `.env.example` را کپی کنید به `.env` و مقادیر کلیدها را پر کنید.

دستورات اصلی
-------------
- نصب: `make install` یا برای dev: `make dev`
- اجرای CLI: `make run`
- اجرای API: `make api` سپس `POST /run` با JSON `{ "task": "..." }`
- تست/لینت: `make test`، `make lint`، `make format`

ساختار
------
- پیکربندی: `configs/` (base + dev/prod overrides)
- ارائه‌دهنده‌ها: `src/providers/` (OpenAI/DeepSeek + Router)
- عامل‌ها: `src/agents/` (researcher/analyst/writer/critic)
- ارکستریشن: `src/orchestration/` (LangGraph، سیاست‌ها، فیدبک)
- ابزارها: `src/tools/` (رجیستری، وب‌گردی ایمن)
- سرویس: `src/services/api.py` (FastAPI)
- مشاهده‌پذیری: `src/core/logging.py`, `src/core/tracing.py`

پیکربندی و امنیت
-----------------
- `APP_ENV=dev|prod` برای انتخاب override.
- کلیدها از env (یا Secret Manager در پروداکشن).
- Redaction ساده در `src/core/security.py` قبل از لاگ‌کردن.

نکات توسعه
----------
- پرامپت‌های عامل‌ها در `prompts/system/` قابل ویرایش هستند.
- Router مدل‌ها در `configs/base.yaml > providers.routing` تنظیم می‌شود.
- برای ارزیابی نمونه، `src/evaluation/` را ببینید.

یادداشت‌ها
---------
- برخی وابستگی‌ها (OpenAI، LangGraph) برای اجرای کامل لازم‌اند.
- تست‌های integration/e2e در صورت نبود وابستگی‌ها به‌طور خودکار skip می‌شوند.

