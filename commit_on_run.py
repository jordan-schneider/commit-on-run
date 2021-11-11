from pathlib import Path
from typing import Union

from fire import Fire  # type: ignore
from git import Head, Refs, Repo  # type: ignore


def set_branch(repo: Repo, branch: Union[str, Head], ref: Union[str, Refs]) -> None:
    repo.head.reference = repo.create_head(branch, ref)
    repo.head.reset(index=True, working_tree=True)


def commit(gitpath: Union[str, Path], branch: str = "runs"):
    repo = Repo(gitpath)
    old_branch = repo.current_head
    if branch not in repo.branches:
        head = repo.create_head(branch)
        head.set_commit("HEAD")
    repo.index.add(gitpath)
    head.set
