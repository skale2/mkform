class RespondingError(Exception):
    NOT_ACCEPTING_RESPONSES = 'form is not accepting responses'

    @classmethod
    def not_accepting_responses(cls):
        raise cls(cls.NOT_ACCEPTING_RESPONSES)