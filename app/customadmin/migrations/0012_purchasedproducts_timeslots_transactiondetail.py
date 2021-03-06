# Generated by Django 3.1.4 on 2020-12-17 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0011_auto_20201214_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('time_slot', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Time Slot',
                'verbose_name_plural': 'Time Slots',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(blank=True, max_length=255, verbose_name='Card Id')),
                ('customer_id', models.CharField(blank=True, max_length=255, verbose_name='Customer Id')),
                ('charge_id', models.CharField(blank=True, max_length=255, verbose_name='Charge Id')),
                ('charge_object', models.CharField(blank=True, max_length=255, null=True, verbose_name='Object')),
                ('amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Amount')),
                ('amount_refunded', models.CharField(blank=True, max_length=255, null=True, verbose_name='Amount refunded')),
                ('application', models.CharField(blank=True, max_length=255, null=True, verbose_name='Application')),
                ('application_fee', models.CharField(blank=True, max_length=255, null=True, verbose_name='Application fee')),
                ('application_fee_amount', models.CharField(blank=True, max_length=255, null=True, verbose_name='Application fee amount')),
                ('balance_transaction', models.CharField(blank=True, max_length=255, verbose_name='Balance transaction')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('calculated_statement_descriptor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calculated statement descriptor')),
                ('captured', models.BooleanField()),
                ('created', models.CharField(blank=True, max_length=255, null=True, verbose_name='Created')),
                ('currency', models.CharField(blank=True, max_length=255, null=True, verbose_name='Currency')),
                ('customer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Customer')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('disputed', models.BooleanField()),
                ('failure_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Failure code')),
                ('failure_message', models.CharField(blank=True, max_length=255, null=True, verbose_name='Failure message')),
                ('fraud_details', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fraud details')),
                ('invoice', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice')),
                ('livemode', models.BooleanField()),
                ('metadata', models.CharField(blank=True, max_length=255, null=True, verbose_name='Metadata')),
                ('on_behalf_of', models.CharField(blank=True, max_length=255, null=True, verbose_name='On behalf of')),
                ('order', models.CharField(blank=True, max_length=255, null=True, verbose_name='Order')),
                ('outcome', models.CharField(blank=True, max_length=255, null=True, verbose_name='Outcome')),
                ('paid', models.BooleanField()),
                ('payment_intent', models.CharField(blank=True, max_length=255, null=True, verbose_name='Payment intent')),
                ('payment_method', models.CharField(blank=True, max_length=255, verbose_name='Card Id')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Brand')),
                ('address_line1_check', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address line1 check')),
                ('address_postal_code_check', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address postal code check')),
                ('cvc_check', models.CharField(blank=True, max_length=255, null=True, verbose_name='CVC check')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Country')),
                ('exp_month', models.CharField(blank=True, max_length=255, null=True, verbose_name='Exp month')),
                ('exp_year', models.CharField(blank=True, max_length=255, null=True, verbose_name='Exp year')),
                ('fingerprint', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fingerprint')),
                ('funding', models.CharField(blank=True, max_length=255, null=True, verbose_name='Funding')),
                ('installments', models.CharField(blank=True, max_length=255, null=True, verbose_name='Installments')),
                ('last4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last4 digit')),
                ('network', models.CharField(blank=True, max_length=255, null=True, verbose_name='Network')),
                ('three_d_secure', models.CharField(blank=True, max_length=255, null=True, verbose_name='3D secure')),
                ('wallet', models.CharField(blank=True, max_length=255, null=True, verbose_name='Wallet')),
                ('charge_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type')),
                ('receipt_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Receipt email')),
                ('receipt_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Receipt number')),
                ('receipt_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Receipt URL')),
                ('refunded', models.BooleanField()),
                ('refunds_object', models.CharField(blank=True, max_length=255, null=True, verbose_name='Refunds object')),
                ('refunds_data', models.CharField(blank=True, max_length=255, null=True, verbose_name='Refunds data')),
                ('refunds_has_more', models.BooleanField()),
                ('refunds_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Refunds URL')),
                ('review', models.CharField(blank=True, max_length=255, null=True, verbose_name='Review')),
                ('shipping', models.CharField(blank=True, max_length=255, null=True, verbose_name='Shipping')),
                ('source_transfer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Source transfer')),
                ('statement_descriptor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Statement descriptor')),
                ('statement_descriptor_suffix', models.CharField(blank=True, max_length=255, null=True, verbose_name='Statement descriptor suffix')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Status')),
                ('transfer_data', models.CharField(blank=True, max_length=255, null=True, verbose_name='Transfer data')),
                ('transfer_group', models.CharField(blank=True, max_length=255, null=True, verbose_name='Transfer group')),
                ('source', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Source')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction Detail',
                'verbose_name_plural': 'Transaction Details',
            },
        ),
        migrations.CreateModel(
            name='PurchasedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('product_price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.shopproduct')),
                ('transaction_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.transactiondetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchased Product',
                'verbose_name_plural': 'Purchased Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
