#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fieldapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
#manage terminal uzerinde komutlari calistirirken kullanilan bir yapidir
#ornek olarak python manage.py runserver ile uygulamayi calistiriyoruz ama bu islemi calistirilacak script icerisinde yapmamiz lazim
#ilgili scripte ulasmak icin terminalde cd fieldapp   -->  ls -->  python manage.py runserver islemleri yapilabilir