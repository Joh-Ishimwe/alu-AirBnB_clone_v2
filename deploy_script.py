from fabric import task, Connection

@task
def do_deploy(c, archive_path):
    if not exists(archive_path):
        return False

    c.put(archive_path, "/tmp/")
    # Other deployment steps...

    return True

