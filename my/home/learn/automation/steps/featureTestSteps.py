from behave import *

use_step_matcher("re")


@given('open "google\.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given open "google.com"')
