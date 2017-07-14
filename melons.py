"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self,
                 species,
                 qty,
                 country_code="USA"):
        """Initialize melon attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.passed_inspection = Falsemar
        # if order_type:
        #     self.order_type = order_type
        # if tax:
        #     self.tax = tax
        # if country_code:
        #     self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"
    country_code = "USA"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize international order with country_code."""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        # Call get_total method from Parent, set = total
        total = super(InternationalMelonOrder, self).get_total()
        # check < condition, add fee to total and return
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the US government."""

    tax = 0.0
    order_type = "government"

    def mark_inspection(self, passed):
        """Record the fact than an order has passed inspection."""

        self.passed_inspection = passed
