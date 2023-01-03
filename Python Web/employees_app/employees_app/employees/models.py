from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AuditEntity):
    dep_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFTUNI = "SoftUni"
    GOOGLE = "Google"
    AMAZON = "Amazon"
    COMPANIES = [SOFTUNI, AMAZON, GOOGLE]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    egn = models.CharField(max_length=10, unique=True, verbose_name='EGN')
    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist')
        )
    )
    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES)
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ("company", "first_name",)


class Project(models.Model):
    name = models.CharField(max_length=30)
    dead_line = models.DateField(null=True, blank=True)
    employees = models.ManyToManyField(to=Employee)
