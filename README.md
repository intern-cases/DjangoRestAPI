# E-commerce discount filter example with Django Rest API

Install
----
Projeyi docker üzerinde çalıştırmak için:
    
    $ git clone git@github.com:intern-cases/DjangoRestAPI.git
    $ cd /Projenin konumu
    $ docker-compose build
    $ docker-compose up -d
    
Start
---
Yeni terminal sekmesinde:

    $ docker exec -it flaskrestapi_app_1 bash
    root:/app# python manage.py makemigrations
    root:/app# python manage.py migrate
    root:/app# python manage.py runserver 0.0.0.0:1881
    
    
    http://0.0.0.0:1881/api-docs
    Swagger ile API endpointlerini ve testleri için kullanabilirsiniz.
    
    
Projenin Amacı ve İşlevi
---
 Kullanıcılar siteye kaydolabilir ve admin yetkisili şirketler için hesap oluşturur. Şirket hesabıyla 
 giriş yapan kullanıcılar kendi bayilerini oluşturabilir ve kayıt olmuş kullanıcı hesapları bayi olarak tanımlanabilir.
 Şirket, bayi, müşteri hesaplarının hepsi konum belirtmek zorundadır.
 
 Bayi hesapları ile giriş yapan kullanıcılar ürün ekleyebilir ve ürünün indirimli olup olmayacağı, aktif olup olmayacağı
 şeklinde ürünü belirleyebilir. Aktif ve indirimli olan ürünler giriş yapmış müşteri hesaplarına konumlarına göre beş km çapında
 olan bayilerin indirimli ürünleri olarak filtrelenir.
 
 ( Bkz: /DjangoRestAPI/Dealer/views.py/DealerListAPIView )
 
