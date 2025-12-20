from rest_framework.throttling import AnonRateThrottle

class AuthThrottle(AnonRateThrottle):
    rate = "5/minute"


class LoginThrottle(AnonRateThrottle):
    rate = "5/minute"
