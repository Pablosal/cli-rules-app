from click.testing import CliRunner
from commands.rules_commands import add_rules


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(add_rules, ['--category', 'yes'])
    assert result.exit_code == 0
