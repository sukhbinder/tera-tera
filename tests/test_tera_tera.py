from tera_tera import cli


def test_create_parser():

    parser = cli.create_parser()
    result = parser.parse_args(["hello"])
    assert result.name == "hello"
