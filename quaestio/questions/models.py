from django.db import models


class Post(models.Model):
    # TODO: Add rating
    # TODO: Link author with a user
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=20)
    created = models.DateTimeField('Created')
    edited = models.DateTimeField('Edited', null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.content


class Tag(models.Model):
    # TODO: Sort out tag creation, author, etc.
    name = models.CharField(max_length=20)


class Question(Post):
    # TODO: Question rating works the same as answer rating?
    tags = models.ManyToManyField(Tag, verbose_name='List of tags')


class Answer(Post):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
