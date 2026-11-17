# ChatGPT Skills

آرشیو نسخه‌دار چهار اسکیل شخصی؛ فایل‌های داخل پوشه‌های اسکیل عین نسخهٔ نصب‌شده ثبت شده‌اند.

| اسکیل | نسخه | تاریخچه |
| --- | --- | --- |
| [اپراتور بک‌تست MT5](skills/fx-mt5-backtest-operator/SKILL.md) | 1.0.0 | [لاگ تغییرات](changelogs/fx-mt5-backtest-operator.md) |
| [حاکمیت مستندات پروژه](skills/project-documentation-governance/SKILL.md) | 1.0.0 | [لاگ تغییرات](changelogs/project-documentation-governance.md) |
| [ممیزی بک‌تست MT5](skills/mt5-backtest-audit/SKILL.md) | 1.0.0 | [لاگ تغییرات](changelogs/mt5-backtest-audit.md) |
| [بازبینی تغییرات ربات MQL5](skills/mql5-change-review/SKILL.md) | 1.0.0 | [لاگ تغییرات](changelogs/mql5-change-review.md) |

## ساختار و نسخه‌بندی

هر اسکیل زیر skills/ پوشهٔ مستقل دارد. [فهرست نسخه‌ها](catalog.json) نسخهٔ جاری را مشخص می‌کند؛ releases/ فهرست فایل‌ها و SHA-256 هر نسخه را نگه می‌دارد. محتوای نسخه‌های گذشته از تاریخچهٔ Git همان نسخه بازیابی می‌شود؛ فایل manifest به‌تنهایی جایگزین فایل‌های قدیمی نیست.

نسخه‌ها مستقل و با الگوی MAJOR.MINOR.PATCH هستند: تغییر ناسازگار = MAJOR، قابلیت سازگار جدید = MINOR، اصلاح سازگار = PATCH. جزئیات در [سیاست انتشار](docs/RELEASE_POLICY.md).

## استفاده

برای ChatGPT، پوشهٔ کامل اسکیل را ارائه کنید و نصب آن را بخواهید. این مخزن با نسخهٔ نصب‌شده در حساب به‌طور خودکار همگام نمی‌شود؛ تغییر و نصب مجدد دو اقدام جدا هستند. برای ابزارهای سازگار، پوشهٔ کامل هر اسکیل شامل SKILL.md، references/، scripts/ و assets/ را مطابق روش نصب همان ابزار استفاده کنید.

## بررسی

Python 3.10+ کافی است؛ برای ابزار بررسی این مخزن وابستگی خارجی لازم نیست.

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 skills/project-documentation-governance/scripts/validate.py --project .
```

[وضعیت جاری](docs/CURRENT_STATE.md)، [نتایج بررسی](docs/TESTING.md)، [قواعد همکاری](AGENTS.md)، [مرجع حقیقت](SOURCE_OF_TRUTH.md) و [تاریخچهٔ مخزن](CHANGELOG.md).
