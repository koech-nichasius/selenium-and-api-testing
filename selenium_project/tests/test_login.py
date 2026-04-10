"""This module contains testcases got User login."""
import pytest

class TestLogin:
    @pytest.mark.parametrize(("test_user", "user_password"),
                             [("admin", "admin")])
    def test_successful_login(self, login_page, test_user, user_password):
        """Test login with correct credentials."""
        login_page.enter_user_name(test_user)
        login_page.enter_password(user_password)
        login_page.tap_login_btn()
        assert login_page.is_login_success()


    @pytest.mark.parametrize(("test_user", "user_password"),
                             [("admin", "admin"),("admin", "admin")])
    def test_unsuccessful_login(self, login_page, test_user, user_password):
        """Test login with wrong credentials."""
        login_page.enter_user_name(test_user)
        login_page.enter_password(user_password)
        login_page.tap_login_btn()
        assert  login_page.is_login_success()
        pytest.xfail("There are no correct or wrong passwords in demo site")

