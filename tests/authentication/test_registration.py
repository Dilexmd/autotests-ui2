import pytest
import allure

from config import settings
from fixtures.pages import registration_form_component
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute



@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
        @pytest.mark.xdist_group(name='authorization-group')
        @allure.title('Registration with correct email, username and password')
        @allure.severity(Severity.CRITICAL)
        def test_successful_registration(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            registration_form_component: RegistrationFormComponent,
            dashboard_toolbar_view_component: DashboardToolbarViewComponent
        ):
                registration_page.visit(AppRoute.REGISTRATION)
                registration_form_component.fill(
                        email=settings.test_user.email,
                        username=settings.test_user.username,
                        password=settings.test_user.password
                )
                registration_page.click_registration_button()
                dashboard_page.dashboard_title.check_visible()