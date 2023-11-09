from django.test import TestCase
from app import models
from .models import BaseCamper

class BaseCamperModelTest(TestCase):
    def test_create_camper(self):
        camper = models.create_camper(
            first_name="John",
            last_name="Doe",
            leadership_team="community",
            module_status="3",
            leave_left_hour="38.5"
        )
        self.assertIsInstance(camper, BaseCamper)
    
    def test_update_module(self):
        camper = models.create_camper(
            first_name="Jane",
            last_name="Smith",
            leadership_team="procurement",
            module_status="2",
            leave_left_hour="45.0"
        )
        updated_camper = models.update_module(camper.id, "5")
        self.assertEqual(updated_camper.module_status, "5")
    
    def test_update_team(self):
        camper = models.create_camper(
            first_name="James",
            last_name="Johnson",
            leadership_team="management",
            module_status="4",
            leave_left_hour="26.5"
        )
        updated_camper = models.update_team(camper.id, "documentation")
        self.assertEqual(updated_camper.leadership_team, "documentation")
    
    def test_update_leave(self):
        camper = models.create_camper(
            first_name="Alice",
            last_name="Anderson",
            leadership_team="community",
            module_status="1",
            leave_left_hour="37.5"
        )
        updated_camper = models.update_leave(camper.id, "55.0")
        self.assertEqual(updated_camper.leave_left_hour, "55.0")
    
    def test_delete_camper(self):
        camper = models.create_camper(
        first_name="Bob",
        last_name="Brown",
        leadership_team="procurement",
        module_status="3",
        leave_left_hour="29.0"
        )
        camper_id = camper.id
        models.delete_camper(camper_id)
        with self.assertRaises(BaseCamper.DoesNotExist):
            deleted_camper = BaseCamper.objects.get(pk=camper_id)


    def test_team_lister(self):
        models.create_camper(
            first_name="Sam",
            last_name="Smith",
            leadership_team="documentation",
            module_status="0",
            leave_left_hour="14.0"
        )
        models.create_camper(
            first_name="Sarah",
            last_name="Johnson",
            leadership_team="documentation",
            module_status="2",
            leave_left_hour="26.0"
        )
        team_members = models.team_lister("documentation")
        self.assertEqual(team_members.count(), 2)

    def test_find_id_by_name(self):
        camper = models.create_camper(
            first_name="John",
            last_name="Doe",
            leadership_team="community",
            module_status="3",
            leave_left_hour="38.5"
        )
        found_id = models.find_id_by_name("John", "Doe")
        self.assertEqual(found_id, camper.id)
    
    def test_all_campers(self):
        models.create_camper(
            first_name="John",
            last_name="Doe",
            leadership_team="community",
            module_status="3",
            leave_left_hour="38.5"
        )
        models.create_camper(
            first_name="Jane",
            last_name="Smith",
            leadership_team="procurement",
            module_status="2",
            leave_left_hour="45.0"
        )

        models.create_camper(
            first_name="James",
            last_name="Johnson",
            leadership_team="management",
            module_status="4",
            leave_left_hour="26.5"
        )
        all_campers = models.all_campers()
        self.assertEqual(all_campers.count(), 3)