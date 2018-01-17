from django.conf import settings
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from work.models import Portfolio
from blog.models import Post, Category, Tag
from new_resume.models import PrivateInformation
from api.rest_framework.serializers import PostSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    def list(self, request):
        portfolio_list = []

        portfolios = Portfolio.objects.filter(is_show=True)
        for portfolio in portfolios:
            portfolio_list.append(
                {
                    "id": portfolio.pk,
                    "title": portfolio.title,
                    "description": portfolio.description,
                    "photoUrl": portfolio.image_url,
                    "link": portfolio.link
                }
            )

        return Response(portfolio_list, status=200)


class PostPagination(PageNumberPagination):
    page_size = 10


class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination

    def list(self, request):
        try:
            queryset = Post.objects.all()

            query_type = request.GET.get("type")
            type_name = request.GET.get("name")

            if query_type and type_name:
                if query_type == "category":
                    queryset = queryset.filter(category__name__icontains=type_name)
                elif query_type == "tag":
                    queryset = queryset.filter(tags__name__icontains=type_name)

            queryset = queryset.order_by("-pk")
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({}, status=400)

    def retrieve(self, request, pk=None):
        post_dict = {}
        post = Post.objects.filter(pk=pk).first()

        if post is not None:
            title = post.title
            content = post.content
            category = post.category.name if post.category else None
            created_date = post.created_date.strftime("%Y년 %m월 %d일 %H:%M")
            tags = [tag.name for tag in post.tags.all()]

            post_dict.update({
                "id": post.pk,
                "title": title,
                "content": content,
                "category": category,
                "createdAt": created_date,
                "tags": tags,
            })

        return Response(post_dict, status=200)


class CategoryViewSet(viewsets.ModelViewSet):
    def list(self, request):
        category_list= []
        categories = Category.objects.annotate(Count('post')).order_by("-post__count")

        for category in categories[:5]:
            category_list.append({"name": category.name})

        return Response(category_list, status=200)


class TagViewSet(viewsets.ModelViewSet):
    def list(self, request):
        tags_list= []
        tags = Tag.objects.all()
        tags = Tag.objects.annotate(Count('post')).order_by("-post__count")

        for tag in tags:
            tags_list.append({"name": tag.name})

        return Response(tags_list, status=200)


class ResumeViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return_dict = {}
        NAME = "KYEONGHOON LEE"
        private_information = PrivateInformation.objects.all().order_by("-pk").first()

        if private_information:
            skills = private_information.skills.all().order_by("-proficiency")
            educations = private_information.educations.all().order_by("-pk")
            experiences = private_information.experiences.all().order_by("-pk")
            self_introductions = private_information.self_introductions.all().order_by("pk")

            private_information_dict = {
                "photoUrl": private_information.photo_url,
                "name": private_information.name,
                "birth": private_information.birth,
                "home": private_information.home,
                "phone": private_information.phone,
                "mail": private_information.email,
                "skills": [
                    {
                        "name": skill.name,
                        "proficiency": skill.proficiency,
                        "description": skill.description
                    } for skill in skills
                ]
            }

            school_list = [
                {
                    "name": education.name,
                    "department": education.department,
                    "periodStart": education.period_start,
                    "periodEnd": education.period_end,
                    "graduation": education.graduation
                } for education in educations
            ]

            experience_list = [
                {
                    "host": experience.host,
                    "periodStart": experience.period_start,
                    "periodEnd": experience.period_end,
                    "projects": [
                        {
                            "name": project.name,
                            "role": project.role,
                            "description": project.description
                        } for project in experience.projects.all().order_by("-pk")
                    ]
                } for experience in experiences
            ]

            self_introduction_list = [
                {
                    "subject": self_introduction.subject,
                    "description": self_introduction.description
                } for self_introduction in self_introductions
            ]

            return_dict.update({
                "name": NAME,
                "privateInformation": private_information_dict,
                "education": {"schools": school_list},
                "experiences": experience_list,
                "selfIntroductions": self_introduction_list
            })

        return_status = 200 if return_dict else 400
        return Response(return_dict, status=return_status)
