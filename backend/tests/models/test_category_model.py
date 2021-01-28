from backend.models.category import Category


class TestCategory:
    name = "Category"
    description = "A very nice category"

    def test_create_instance(self):
        self.category = Category(self.name, self.description)
        assert isinstance(self.category, Category)
        assert self.category.name == self.name
        assert self.category.description == self.description

    def test_invalid_name(self):
        invalid_names = ['', 123, 'a' * 1000]
        for value in invalid_names:
            self.name = value
            try:
                self.category = Category(self.name, self.description)
            except Exception as e:
                assert isinstance(e, ValueError)

    def test_invalid_description(self):
        invalid_descriptions = ['', 123, 'a' * 1000]
        for value in invalid_descriptions:
            self.description = value
            try:
                self.category = Category(self.name, self.description)
            except Exception as e:
                assert isinstance(e, ValueError)
