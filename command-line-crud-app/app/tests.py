from django.test import TestCase
from app import models
from .models import BaseCamper

class BaseCamperModelTest(TestCase):
    def test_create_camper(self):
        camper = models.create_camper(
            first_name="John",
            last_name="Doe",
            leadership_team="Team A",
            module_status="InProgress",
            leave_left_hour="8.5"
        )
        self.assertIsInstance(camper, BaseCamper)
    
    def test_update_module(self):
        camper = models.create_camper(
            first_name="Jane",
            last_name="Smith",
            leadership_team="Team B",
            module_status="NotStarted",
            leave_left_hour="10.0"
        )
        updated_camper = models.update_module(camper.id, "Completed")
        self.assertEqual(updated_camper.module_status, "Completed")
    
    def test_update_team(self):
        camper = models.create_camper(
            first_name="James",
            last_name="Johnson",
            leadership_team="Team C",
            module_status="InProgress",
            leave_left_hour="6.5"
        )
        updated_camper = models.update_team(camper.id, "Team D")
        self.assertEqual(updated_camper.leadership_team, "Team D")
    
    def test_update_leave(self):
        camper = models.create_camper(
            first_name="Alice",
            last_name="Anderson",
            leadership_team="Team E",
            module_status="Completed",
            leave_left_hour="5.0"
        )
        updated_camper = models.update_leave(camper.id, "7.5")
        self.assertEqual(updated_camper.leave_left_hour, "7.5")
    
    def test_delete_camper(self):
        camper = models.create_camper(
            first_name="Bob",
            last_name="Brown",
            leadership_team="Team F",
            module_status="NotStarted",
            leave_left_hour="9.0"
        )
        camper_id = camper.id
        deleted_camper = models.delete_camper(camper_id)
        self.assertEqual(deleted_camper,None)

    def test_team_lister(self):
        models.create_camper(
            first_name="Sam",
            last_name="Smith",
            leadership_team="Team G",
            module_status="InProgress",
            leave_left_hour="4.0"
        )
        models.create_camper(
            first_name="Sarah",
            last_name="Johnson",
            leadership_team="Team G",
            module_status="NotStarted",
            leave_left_hour="6.0"
        )
        team_members = models.team_lister("Team G")
        self.assertEqual(team_members.count(), 2)

