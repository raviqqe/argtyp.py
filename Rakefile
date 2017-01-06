task :test do
  sh 'pytest --doctest-modules argtyp'
end


task :upload => %i(clean test) do
  sh 'python3 setup.py sdist bdist_wheel'
  sh 'twine upload dist/*'
end


task :clean do
  sh 'git clean -dfx'
end
