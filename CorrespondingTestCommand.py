import sublime
import sublime_plugin
import re
import os

def find_corresponding_test(file_path):
  # file_path_parts = file_path.split('app/');
  # project_file_path = file_path_parts[1];
  # test_filename = project_file_path.replace(".rb", "_spec.rb")
  # test_file_path = file_path_parts[0] + "spec/" + test_filename
  # return test_file_path;
  return file_path.replace('app', 'spec').replace('.rb', '_spec.rb');

class CorrespondingTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    current_file = self.view.file_name();
    if not re.search('/voice/', current_file):
      return;

    test_file = find_corresponding_test(current_file);
    print(test_file);

    if os.path.isfile(test_file):
      print("EXISTS!");
      self.view.window().open_file(test_file);

    return;
