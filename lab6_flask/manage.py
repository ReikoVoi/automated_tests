import unittest
import os
import coverage
from coverage import python

from flask_script import Manager

import db_create_users

#python db_create_users.py
from project import app, db

manager = Manager(app)

@manager.command
def test():
    """Запуск тестов."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def cov():
    """Запуск тестов и расчет покрытия кода."""
    cov = coverage.coverage(
        branch=True,
        include='project/*'
    )
    cov.start()
    """Запуск тестов."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    # вывод оценки покрытия на консоль
    print('Coverage Summary:')
    cov.report()
    # создание пути к папке coverage внутри проекта
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    # вывод HTML-отчета о покрытии в папку coverage внутри проекта
    cov.html_report(directory=covdir)
    print('Saved to: ' + covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()
