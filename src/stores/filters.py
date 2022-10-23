from rest_framework_gis.filters import DistanceToPointOrderingFilter


class RegionFilter(DistanceToPointOrderingFilter):
    def filter_queryset(self, request, queryset, _):
        point = self.get_filter_point(request)
        if not point:
            return queryset

        return queryset.filter(coverage_area__contains=point)
