from rest_framework import serializers
from .models import StaffBase, Manager, Intern


class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']
    def get_role():
        return 'Staff'
    
class ManagerSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Manager
        fields = StaffBaseSerializer.Meta.fields + ['position', 'department', 'has_company_card', 'date_joined']
        read_only_fields = ['date_joined', 'has_company_card']
    def get_role(self, obj):
            return 'Manager'
    
class InternSerializer(StaffBaseSerializer):
    manager = ManagerSerializer(read_only=True)
    class Meta(StaffBaseSerializer.Meta):
        model = Intern
        fields = StaffBaseSerializer.Meta.fields + ['position', 'department', 'mentor', 'date_joined', 'internship_end']
        read_only_fields = ['mentor', 'date_joined']
        