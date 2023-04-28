import sublime
import sublime_plugin
import re
import os

def find_corresponding_test(file_path):
  file_path_parts = file_path.split('app/');
  project_file_path = file_path_parts[1];
  # filename = project_file_path.split('/')[-1]
  test_filename = project_file_path.replace(".rb", "_spec.rb")
  test_file_path = file_path_parts[0] + "spec/" + test_filename

  # spec/task_adapter/consumers/task_events_consumer_spec.rb
  return test_file_path;

class CorrespondingTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    current_file = self.view.file_name();
    # /Users/david.mcginn/Code/zendesk/voice/app/task_adapter/consumers/task_events_consumer.rb
    test_file = find_corresponding_test(current_file);
    print(test_file);

    if os.path.isfile(test_file):
      print("EXISTS!");
      self.view.window().open_file(test_file);

    return;
