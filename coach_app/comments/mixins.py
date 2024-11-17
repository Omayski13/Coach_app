class CommentTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].required = True
        self.fields['content'].label = "Добави коментар"
        self.fields['content'].widget.attrs.update({
            'class': 'wide-input-comments'
        })