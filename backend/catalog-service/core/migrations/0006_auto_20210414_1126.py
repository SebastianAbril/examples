# Generated by Django 3.1.2 on 2021-04-14 11:26
import csv

from django.db import migrations

from core.shared.base.domain.uuid import UUID


def items_data(apps, schema_editor):
    TypeModel = apps.get_model('core', 'TypeModel')
    BrandModel = apps.get_model('core', 'BrandModel')
    ItemModel = apps.get_model('core', 'ItemModel')

    with open('core/migrations/items.csv') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        items = []

        for row in reader:
            type_model = TypeModel.objects.get(name=row[0])
            brand_model = BrandModel.objects.get(name=row[1])

            item = ItemModel(
                id=UUID.random(),
                brand_id=brand_model.id,
                type_id=type_model.id,
                name=row[3],
                description=row[2],
                picture_file_name=row[5],
                price=float(row[4])
            )

            items.append(item)

        ItemModel.objects.bulk_create(items)


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_itemmodel'),
    ]

    operations = [
        migrations.RunPython(items_data),
    ]
