from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Ac0Qp1rVpiWmM4wI8eQKG_Tw-qyKJRNbtxJ8jvLUefQWNfc182JbfJHheBvgJJTv-90d8JShpdw5KOKN"
        self.client_secret = "ENB5YFnhLm4-hQh5EvBLpFu6-vPlglTWoB1KU0Yh8zDuDYe58JHbc1sZfpsaR1u85AH4LMXngwBNbuVu"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
