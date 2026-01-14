import pytest
from playwright.sync_api import Page

from pages.courses.courses_list_page import CoursesListPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.create_course_page import CreateCoursePage
from components.charts.chart_view_component import ChartViewComponent

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)

@pytest.fixture
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)

@pytest.fixture
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)

@pytest.fixture
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)

@pytest.fixture
def login_form_component(login_page: LoginPage):
    return login_page.login_form

@pytest.fixture
def registration_form_component(registration_page: RegistrationPage):
    return registration_page.registration_form

@pytest.fixture
def dashboard_toolbar_view_component(dashboard_page: DashboardPage):
    return dashboard_page.dashboard_title

@pytest.fixture
def students_chart_component(dashboard_page: DashboardPage) -> ChartViewComponent:
    return dashboard_page.students_chart

@pytest.fixture
def activities_chart_component(dashboard_page: DashboardPage) -> ChartViewComponent:
    return dashboard_page.activities_chart

@pytest.fixture
def courses_chart_component(dashboard_page: DashboardPage) -> ChartViewComponent:
    return dashboard_page.courses_chart

@pytest.fixture
def scores_chart_component(dashboard_page: DashboardPage) -> ChartViewComponent:
    return dashboard_page.scores_chart
