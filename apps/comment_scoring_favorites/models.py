from django.db import models
from apps.products.models import Product
from apps.accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator



class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='comments_product')
    commenting_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر نظر دهنده', related_name='comments_user1')
    approving_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر تایید کننده نظر', related_name='comments_user2')
    comment_text = models.TextField(verbose_name='متن نظر')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت نظر')
    comment_parent = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد نطر', related_name='comment_child')
    
    def __str__(self) -> str:
        return f"{self.product} - {self.commenting_user}"
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        
        
        
class Scoring(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='scoring_product')
    scoring_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر امتیاز دهنده', related_name='scoring_user1')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='امتیاز')
    
    def __str__(self) -> str:
        return f"{self.product} - {self.scoring_user}"
    
    class Meta:
        verbose_name = 'امتیاز'
        verbose_name_plural = 'امتیازات'
        
        
        
class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='favorite_product')
    favorite_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر علاقه مند', related_name='favorite_user1')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')
    
    def __str__(self) -> str:
        return f"{self.product} - {self.favorite_user}"
    
    class Meta:
        verbose_name = 'علاقه'
        verbose_name_plural = 'علایق'
