from django.db import models

# Create your models here.
cateroies=(
    ('housing', 'Housing'),
        ('utilities', 'Utilities'),
        ('food', 'Food & Groceries'),
        ('transportation', 'Transportation'),
        ('health', 'Health & Medical'),
        ('entertainment', 'Entertainment'),
        ('fitness', 'Fitness & Sports'),
        ('shopping', 'Shopping'),
        ('personal_care', 'Personal Care'),
        ('subscriptions', 'Subscriptions & Memberships'),
        ('debt', 'Debt Repayments'),
        ('savings', 'Savings & Investments'),
        ('insurance', 'Insurance'),
        ('taxes', 'Taxes'),
        ('education', 'Education'),
        ('gifts', 'Gifts & Donations'),
        ('childcare', 'Childcare'),
        ('travel', 'Travel'),
        ('emergency', 'Emergency Expenses'),
        ('misc', 'Miscellaneous'),
)
transaction=(
    ('expenses','expenses'),
    ("income",'income')
)
class User(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    profile_img=models.ImageField(upload_to="media",blank=True,null=True)
    
    def __str__(self):
        return self.name
class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=30,choices=transaction,blank=True,null=True)
    transaction_amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    category=models.CharField(max_length=30,choices=cateroies,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    desc=models.TextField(blank=True,null=True)
    balance=models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.transaction_type