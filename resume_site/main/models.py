import nh3
from django.db import models

ALLOWED_HTML_TAGS = {"p", "br", "strong", "em", "b", "i", "ul", "ol", "li", "a"}


def sanitize_html(value):
    return nh3.clean(value, tags=ALLOWED_HTML_TAGS)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField(help_text="Короткий абзац «Обо мне»")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.about = sanitize_html(self.about)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SkillGroup(models.Model):
    """Группа навыков — например, «Языки и технологии»."""
    title = models.CharField(
        max_length=100, help_text="Например: Языки и технологии")
    items = models.CharField(
        max_length=300,
        help_text="Через запятую: Python, SQL, HTML, CSS"
    )
    order = models.PositiveIntegerField(
        default=0, help_text="Порядок вывода (0, 1, 2...)")

    class Meta:
        ordering = ['order']
        verbose_name = "Группа навыков"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title


class Experience(models.Model):
    """Место работы."""
    position = models.CharField(max_length=200, help_text="Должность")
    company = models.CharField(
        max_length=200, blank=True, help_text="Компания (если есть)")
    period = models.CharField(
        max_length=100, help_text="Например: Октябрь 2024 — настоящее время")
    description = models.TextField(
        help_text="Пункты списка. Каждый пункт — с новой строки.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"{self.position} — {self.company}" if self.company else self.position


class Project(models.Model):
    """Проект."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(
        blank=True, help_text="Ссылка на GitHub или демо (необязательно)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class Education(models.Model):
    """Образование."""
    institution = models.CharField(max_length=200, help_text="Вуз")
    program = models.CharField(
        max_length=200, help_text="Направление / программа")
    period = models.CharField(
        max_length=100, blank=True, help_text="Например: 3-й курс")
    note = models.TextField(
        blank=True, help_text="Дополнительные детали (необязательно)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def save(self, *args, **kwargs):
        if self.note:
            self.note = sanitize_html(self.note)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.institution
