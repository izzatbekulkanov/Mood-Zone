import json

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt


def group_list(request):
    groups = Group.objects.all().order_by('-id')  # Id bo'yicha teskari tartibda
    group_data = []

    for group in groups:
        users = [{'initials': user.username} for user in group.user_set.all()]
        group_info = {'id': group.id, 'name': group.name, 'users': users}
        group_data.append(group_info)

    return JsonResponse(group_data, safe=False)


def group_detail(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        group_data = {'id': group.id, 'name': group.name}
        return JsonResponse(group_data)
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group not found'}, status=404)


def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            group = Group.objects.create(name=name)
            return JsonResponse({'success': 'Group created successfully', 'id': group.id})
        else:
            return JsonResponse({'error': 'Name field is required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def update_group(request, group_id):
    if request.method == 'PUT':
        try:
            group = Group.objects.get(id=group_id)
            name = request.PUT.get('name')
            if name:
                group.name = name
                group.save()
                return JsonResponse({'success': 'Group updated successfully'})
            else:
                return JsonResponse({'error': 'Name field is required'}, status=400)
        except Group.DoesNotExist:
            return JsonResponse({'error': 'Group not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)


def delete_group(request, group_id):
    if request.method == 'DELETE':
        try:
            group = Group.objects.get(id=group_id)
            group.delete()
            return JsonResponse({'success': 'Group deleted successfully'})
        except Group.DoesNotExist:
            return JsonResponse({'error': 'Group not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)


def group_permissions(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
        all_permissions = Permission.objects.all()
        group_permissions = group.permissions.all()

        permission_data = []
        for perm in all_permissions:
            permission_data.append({
                'name': perm.name,
                'permission': perm.codename,
                'selected': perm in group_permissions  # Tekshirish
            })

        return JsonResponse(permission_data, safe=False)
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def save_group_permissions(request, group_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=group_id)
        permissions_data = json.loads(request.body.decode('utf-8'))
        for permission_name in permissions_data['permissions']:
            permission = get_object_or_404(Permission, name=permission_name)
            group.permissions.add(permission)
        for unchecked_permission_name in permissions_data.get('unchecked_permissions', []):
            unchecked_permission = get_object_or_404(Permission, name=unchecked_permission_name)
            group.permissions.remove(unchecked_permission)
        return JsonResponse({'success': 'Permissions saved successfully'})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def permissions_api(request):
    if request.method == 'GET':
        permissions = Permission.objects.all()
        content_types = ContentType.objects.all()

        permissions_data = [{
            'id': perm.id,
            'name': perm.name,
            'codename': perm.codename,
            'content_type_id': perm.content_type_id,
            'content_type_name': perm.content_type.name,
            'content_type_app_label': perm.content_type.app_label,
        } for perm in permissions]

        content_types_data = [{
            'id': content_type.id,
            'name': content_type.name,
            'app_label': content_type.app_label,
        } for content_type in content_types]

        return JsonResponse({
            'permissions': permissions_data,
            'content_types': content_types_data,
        })
    else:
        return JsonResponse({'error': 'Faqat GET usuli qo‘llaniladi'}, status=405)



def save_permission(request):
    if request.method == 'POST':
        try:
            # POST so'rovini qabul qilish va ma'lumotlarni tekshirish
            data = json.loads(request.body)
            permission_id = data.get('id')
            permission_name = data.get('name')
            permission_codename = data.get('codename')
            permission_content_type_id = data.get('content_type_id')

            # Permissionni bazada izlash
            permission = Permission.objects.get(pk=permission_id)

            # Permissionni yangilash yoki qo'shish
            permission.name = permission_name
            permission.codename = permission_codename
            permission.content_type_id = permission_content_type_id
            permission.save()

            # Agar ma'lumotlar muvaffaqiyatli saqlansangiz
            return JsonResponse({'status': 'success', 'message': permission_codename+' muvaffaqiyatli saqlandi'})
        except Exception as e:
            # Xatolik sodir bo'lganda
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Faqat POST so\'rovlarni qo\'llashingiz mumkin'}, status=405)