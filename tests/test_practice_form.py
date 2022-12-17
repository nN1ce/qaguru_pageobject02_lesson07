import datetime

from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.model.controls import datepicker
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.data import user
from demoqa_tests.model.data.user import User, Gender


def test_submit_filled_form():
    (
        app.practice_page.open()

        .fill_name('Evgen', 'Lukyanov')
        .fill_email('lukyanov@qaguru.com')
        .fill_gender(user.Gender.Male)
        .fill_birthday(datetime.date(1990, 5, 4))
        .fill_phone('8911120121')
        .fill_subjects('Maths', 'English', 'Computer Science')
        .fill_hobbies(user.Hobby.Music, user.Hobby.Reading)
        .select_picture('../resources/photo.jpg')
        .fill_address('Russia Saint-P Moskovskaya 20')
        .select_state('NCR')
        .select_city('Gurgaon')
        .submit_form()

        .assert_form_sent(
            ('Student Name', 'Evgen Lukyanov'),
            ('Student Email', 'lukyanov@qaguru.com'),
            ('Gender', Gender.Male.name),
            ('Mobile', '8911120121'),
            ('Date of Birth', datetime.date(1990, 5, 4)),
            ('Subjects', 'Maths, English, Computer Science'),
            ('Hobbies', f'{user.Hobby.Music.value}, {user.Hobby.Reading.value}'),
            ('Picture', 'photo.jpg'),
            ('Address', 'Russia Saint-P Moskovskaya 20'),
            ('State and City', 'NCR Gurgaon'),
        )
    )


def test_submit_filled_form_():
    """
    potential version of higher level StepsObject + DataObject implementation
    """
    lev = User(
        first_name='Evgen',
        last_name='Lukyanov',
        email='lukyanov@qaguru.com',
        # TODO: implement more fields
    )

    app.practice_page.open().register(lev).assert_registered(lev)  # TODO: implement these methods so code works


def test_submit_filled_form__():
    """
    intermediate version of lesson, in the middle of applying OOP paradigm to datepicker implementation
    """
    app.practice_page.open()

    ...  # beginning of the test

    birthday = DatePicker(browser.element('#dateOfBirthInput'))
    birthday.set_date(datetime.date(1990, 5, 4)).assert_value(datetime.date(1990, 5, 4))
    '''
    # or simply (without variable)
    DatePicker(browser.element('#dateOfBirthInput')).set_date(
        datetime.date(1990, 5, 4)
    ).assert_value(datetime.date(1990, 5, 4))

    # not fluent version:
    birthday = DatePicker(browser.element('#dateOfBirthInput'))
    birthday.set_date(datetime.date(1990, 5, 4))
    birthday.assert_value(datetime.date(1990, 5, 4))

    # actual version that Python does under the hood:
    birthday = object.__new__(DatePicker)  # noqa
    DatePicker.__init__(birthday, browser.element('#dateOfBirthInput'))
    DatePicker.set_date(birthday, datetime.date(1990, 5, 4))
    DatePicker.assert_value(birthday, datetime.date(1990, 5, 4))

    # just pure modules with «pure» procedures
    birthday = browser.element('#dateOfBirthInput')
    datepicker.set_date(birthday, datetime.date(1990, 5, 4))
    datepicker.assert_value(birthday,  datetime.date(1990, 5, 4))

    # the following version would be too much,
    # because we start to miss test data from places where it should be used
    # to emphasize test logic
    DatePicker(browser.element('#dateOfBirthInput'), datetime.date(1990, 5, 4)).set_date().assert_value()
    '''

    # graduation = DatePicker(browser.element('#dateOfGraduation'))
    # graduation.set_date(datetime.date(2007, 7, 29))

    ...  # ending of the test
