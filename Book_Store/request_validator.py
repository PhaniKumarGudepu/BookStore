from Book_Store.exceptions import InvalidRequest


# validates requests of Books
class Books_validator:

    # validates get_books_list request
    def validate_get_books_list(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('category') or kwargs.get('category') is '':
                raise InvalidRequest(f'Path parameter <category> is empty')
            function(**kwargs)
        return wrapper

    # validates get_book request
    def validate_get_book(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('book_id') or kwargs.get('book_id') is '':
                raise InvalidRequest(f'Path parameter <book_id> is empty')
            function(**kwargs)
        return wrapper


# validates requests of Baskets
class Basket_validator:
    # validates get_basket request
    def validate_get_basket(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('user_id') or kwargs.get('user_id') is '':
                raise InvalidRequest(f'Path parameter <user_id> is empty')
            if not kwargs.get('basket_id') or kwargs.get('basket_id') is '':
                raise InvalidRequest(f'Path parameter <basket_id> is empty')
            function(**kwargs)
        return wrapper

    # validates update_basket request
    def validate_update_basket(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('user_id') or kwargs.get('user_id') is '':
                raise InvalidRequest(f'Path parameter <user_id> is empty')
            if not kwargs.get('basket_id') or kwargs.get('basket_id') is '':
                raise InvalidRequest(f'Path parameter <basket_id> is empty')
            if not kwargs.get('body') or kwargs.get('body') is {}:
                raise InvalidRequest(f'Request body is empty')
            if not kwargs.get('body').get('book_id') or kwargs.get('body').get('book_id') is '':
                raise InvalidRequest(f'Body parameter <book_id> is empty')
            function(**kwargs)
        return wrapper

    # validates delete_basket_item request
    def validate_delete_basket_item(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('user_id') or kwargs.get('user_id') is '':
                raise InvalidRequest(f'Path parameter <user_id> is empty')
            if not kwargs.get('basket_id') or kwargs.get('basket_id') is '':
                raise InvalidRequest(f'Path parameter <basket_id> is empty')
            if not kwargs.get('body') or kwargs.get('body') is {}:
                raise InvalidRequest(f'Request body is empty')
            if not kwargs.get('body').get('book_id') or kwargs.get('body').get('book_id') is '':
                raise InvalidRequest(f'Body parameter <book_id> is empty')
            function(**kwargs)
        return wrapper

    # validates create_basket request
    def validate_create_basket(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('user_id') or kwargs.get('user_id') is '':
                raise InvalidRequest(f'Path parameter <user_id> is empty')
            if not kwargs.get('body') or kwargs.get('body') is {}:
                raise InvalidRequest(f'Request body is empty')
            if not kwargs.get('body').get('book_id') or kwargs.get('body').get('book_id') is '':
                raise InvalidRequest(f'Body parameter <book_id> is empty')
            function(**kwargs)
        return wrapper


# validated requests of Orders
class Order_validator:
    # validates place_order request
    def validate_place_order(self, function):
        def wrapper(**kwargs):
            if not kwargs.get('user_id') or kwargs.get('user_id') is '':
                raise InvalidRequest(f'Path parameter <user_id> is empty')
            if not kwargs.get('basket_id') or kwargs.get('basket_id') is '':
                raise InvalidRequest(f'Path parameter <basket_id> is empty')
            if not kwargs.get('body') or kwargs.get('body') is {}:
                raise InvalidRequest(f'Request body is empty')
            if not kwargs.get('body').get('name') or kwargs.get('body').get('name') is '':
                raise InvalidRequest(f'Body parameter <name> is empty')
            if not kwargs.get('body').get('email') or kwargs.get('body').get('email') is '':
                raise InvalidRequest(f'Body parameter <email> is empty')
            if not kwargs.get('body').get('phone') or kwargs.get('body').get('phone') is '':
                raise InvalidRequest(f'Body parameter <phone> is empty')
            function(**kwargs)
        return wrapper
