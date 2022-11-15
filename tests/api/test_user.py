from api.user import (
    create_user,
    get_executive,
    get_executives,
    get_user,
    get_users,
    update_user_bio,
    update_executive_status,
    update_user_name,
)


def test_create_user(db, user):
    db_user = create_user(db=db, new_user=user)

    assert db_user.name == "blackprince"
    assert db_user.bio is not None
    assert db_user.id
    assert db_user.is_executive is False


def test_get_users(db, user):
    entry = create_user(db=db, new_user=user)
    db_user = get_user(db=db, user_id=entry.id)
    db_users = get_users(db=db)

    assert db_user.name == "blackprince"
    assert db_users != []


def test_create_executive(db, executive):
    db_executive = create_user(db=db, new_user=executive)

    assert db_executive.name == "Trump"
    assert db_executive.bio is not None
    assert db_executive.id == 2
    assert db_executive.is_executive is True


def test_get_executives(db, executive):
    entry = create_user(db=db, new_user=executive)
    executive = get_executive(db=db, user_id=entry.id)
    executives = get_executives(db=db)

    assert executive.name == "Trump"
    assert executives != []


def test_update_user_bio(db, user):
    entry = create_user(db=db, new_user=user)
    new_bio = """The problem is that you are not adequate, the problem is, you think you should be."""
    db_user = update_user_bio(db=db, new_bio=new_bio, user_id=entry.id)

    assert db_user.bio == new_bio
    assert db_user.name == "blackprince"


def test_update_user_name(db, user):
    entry = create_user(db=db, new_user=user)
    new_name = "Black King Kong"
    db_user = update_user_name(db=db, user_id=entry.id, new_name=new_name)

    assert db_user.name == new_name
    assert db_user.is_executive is False


def test_update_executive_status(db, executive):
    db_executive = update_executive_status(db=db, user_id=executive.id)

    assert db_executive.is_executive is False
    assert db_executive.name == "Trump"
