# Generated by Django 5.1.6 on 2025-05-03 20:07

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('td_file', models.FileField(blank=True, null=True, upload_to='courses/td/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('tp_file', models.FileField(blank=True, null=True, upload_to='courses/tp/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('correction', models.FileField(blank=True, null=True, upload_to='courses/corrections/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assignments/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_submissions', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_submissions', to='enseignants.course')),
            ],
        ),
        migrations.CreateModel(
            name='EnseignantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='enseignants/cvs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('publications', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enseignant_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='enseignants.formation')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='enseignants.formation'),
        ),
    ]
