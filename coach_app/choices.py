from django.db import models


class AccountsLicenceChoices(models.TextChoices):
    UEFA_PRO = 'Uefa PRO', 'Uefa PRO'
    UEFA_A = 'Uefa A', 'Uefa A'
    UEFA_B = 'Uefa B', 'Uefa B'
    UEFA_C = 'Uefa C', 'Uefa C'
    NATIONAL_C = 'National C', 'National C'
    GRASSROOTS_D = 'Grassroots D', 'Grassroots D'
    NONE = 'Без лиценз', 'Без лиценз'



class AgeGroupsChoices(models.TextChoices):
    U6 = 'U5 - U6', 'U5 - U6'
    U8 = 'U7 - U8', 'U7 - U8'
    U10 = 'U9 - U10', 'U9 - U10'
    U12 = 'U11 - U12', 'U11 - U12'
    U14 = 'U13 - U14', 'U13 - U14'
    U16 = 'U15 - U16', 'U15 - U16'
    U19 = 'U16 - U19', 'U16 - U19'
    SENIOR = 'Мъже', 'Мъже'
