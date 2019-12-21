class URLException(Exception):

    def __init__(self, error=None):
        self.error = error
        
    def __repr__(self):
        return 'img not found'


class CV2Exception(Exception):

    def __init__(self, error=None):
        self.error = error

    def __repr__(self):
        return 'cv2 error'
