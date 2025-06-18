import importlib
import sys


def test_jobs_runs(monkeypatch, capsys):
    # fake data structures used by the script
    class FakePost:
        def __init__(self):
            self.title = "title"
            self.id = "id"
            self.author = "author"
            self.url = "url"
            self.num_comments = 0

    class FakeComment:
        def __init__(self):
            self.body = "body"
            self.author = "commenter"

    class FakeSubreddit:
        def top(self, limit=None):
            return [FakePost()]

        def new(self, limit=None):
            return [FakePost()]

    class FakeSubmission:
        def __init__(self):
            self.comments = [FakeComment() for _ in range(5)]

    class FakeReddit:
        def subreddit(self, name):
            return FakeSubreddit()

        def submission(self, id=None):
            return FakeSubmission()

    class FakePraw:
        def Reddit(self, *args, **kwargs):
            return FakeReddit()

    # Patch the praw module before importing jobs
    monkeypatch.setitem(sys.modules, "praw", FakePraw())

    if "jobs" in sys.modules:
        del sys.modules["jobs"]
    import jobs
    importlib.reload(jobs)

    output = capsys.readouterr().out
    assert "Title -" in output
    assert "Printing comment..." in output

