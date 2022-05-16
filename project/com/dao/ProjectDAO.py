from project import db
from project.com.vo.ProjectVO import ProjectVO

class ProjectDAO:
    def insertProject(self, projectVO):
        db.session.add(projectVO)
        db.session.commit()

    def fetchProjects(self, projectVO):
        projects_list = ProjectVO.query.filter_by(project_loginId = projectVO.project_loginId).all()
        return projects_list

    def deleteProject(self, projectVO):
        ProjectVO.query.filter_by(Id=projectVO.Id).delete()
        db.session.commit()

    def updateProject(self, projectsVO):
        # projects_list = ProjectsVO.query.filter_by(Id = projectsVO.Id).first()
        # projects_list.project_title = projectsVO.project_title
        # projects_list.project_detail = projectsVO.project_detail
        # projects_list.project_loginId = projectsVO.project_loginId
        db.session.merge(projectsVO)
        db.session.commit()
